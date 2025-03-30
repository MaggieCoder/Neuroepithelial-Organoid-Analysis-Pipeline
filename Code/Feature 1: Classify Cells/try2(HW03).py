// ---------------------------------------
// 1. Open and preprocess the image
// ---------------------------------------

// Define the file path
filePath = "C:/Users/geshan/OneDrive - Michigan Medicine/Desktop/tiff/WIP006_G10A.tif";

// Check if the file exists
if (!File.exists(filePath)) {
    print("Error: File does not exist at the specified path: " + filePath);
    exit();
}

// Close all open images to avoid confusion
run("Close All");

// Open the image
open(filePath);

// Confirm that the image is open
if (nImages == 0) {
    print("Error: Failed to open the image. Please check the file path and permissions.");
    exit();
}

// Get and print the original title
originalTitle = getTitle();
print("Original Title: " + originalTitle);

// Optionally, rename the image to a fixed name to avoid issues
rename("Original_Image");
originalTitle = "Original_Image";
print("Image renamed to: " + originalTitle);

// Verify the renaming
currentTitle = getTitle();
print("Current Image Title: " + currentTitle);
if (currentTitle != originalTitle) {
    print("Error: Renaming failed. Current title is " + currentTitle);
    exit();
}

// Get the Image ID for reliable selection
originalImageID = getImageID();
print("Original_Image ID: " + originalImageID);

// Set ScaleConversions option
setOption("ScaleConversions", true);

// Convert to 8-bit and invert (if needed)
selectImage(originalImageID);
run("8-bit");
run("Invert");

// Optional smoothing/denoising
run("Smooth");

// -----------------------------------------------------
// 2. Segment the entire cell ("Whole_Cell")
// -----------------------------------------------------
setAutoThreshold("Default dark no-reset"); // Adjust threshold method as needed
run("Convert to Mask");
run("Close-"); // Clean up the mask

// Clear ROI Manager before adding new ROIs
roiManager("reset");

// Use Analyze Particles to detect the cell region
run("Analyze Particles...", "size=0-Infinity exclude clear add");
if (roiManager("count") == 0) {
    print("Error: No particles detected for Whole_Cell. Check thresholding.");
    exit();
}

// Rename the ROI to "Whole_Cell" and measure its area
roiManager("Select", 0);
roiManager("Rename", "Whole_Cell");
roiManager("Measure");
wholeCellArea = getResult("Area", nResults - 1); // Store the area

// -------------------------------------------
// 3. Segment the "Apical_Out" region
// -------------------------------------------
selectImage(originalImageID);
run("Duplicate...", "title=apical_out_tmp");
apicalOutTempID = getImageID();
print("Apical_Out Temporary Image ID: " + apicalOutTempID);

// Apply threshold or other segmentation steps for the apical-out region
selectImage(apicalOutTempID);
setAutoThreshold("Default dark no-reset");
run("Convert to Mask");
run("Close-");

// Clear ROI Manager before adding new ROIs
roiManager("reset");

// Use Analyze Particles to detect the apical-out region
run("Analyze Particles...", "size=200-Infinity exclude clear add");
if (roiManager("count") == 0) {
    print("Error: No particles detected for Apical_Out. Check thresholding.");
    exit();
}

// Rename and measure the "Apical_Out" region
roiManager("Select", roiManager("count") - 1);
roiManager("Rename", "Apical_Out");
roiManager("Measure");
apicalOutArea = getResult("Area", nResults - 1);

// Close the temporary apical_out image
selectImage(apicalOutTempID);
run("Close");

// ------------------------------------------------------
// 4. Derive the "Apical_In" region = Whole_Cell - Apical_Out
// ------------------------------------------------------

// -------------------------------------------
// Alternative Method: Using Image Masks
// -------------------------------------------

// Step 1: Create a binary mask for Whole_Cell
roiManager("Select", "Whole_Cell");
run("Duplicate...", "title=whole_cell_mask");
wholeCellMaskID = getImageID();
print("Whole_Cell Mask ID: " + wholeCellMaskID);

// Convert to Binary Mask
selectImage(wholeCellMaskID);
run("Make Binary");

// Step 2: Create a binary mask for Apical_Out
roiManager("Select", "Apical_Out");
run("Duplicate...", "title=apical_out_mask");
apicalOutMaskID = getImageID();
print("Apical_Out Mask ID: " + apicalOutMaskID);

// Convert to Binary Mask
selectImage(apicalOutMaskID);
run("Make Binary");

// Step 3: Subtract Apical_Out Mask from Whole_Cell Mask
selectImage(wholeCellMaskID);
run("Image Calculator...", "image1=whole_cell_mask operation=Subtract image2=apical_out_mask create");

// The result is the "Apical_In" mask
resultImageID = getImageID(); // ID of the result image
selectImage(resultImageID);
run("Set Scale...", "distance=0 known=0 unit=Unknown"); // Reset scale if needed
run("Convert to Mask");

// Add the "Apical_In" ROI to ROI Manager
run("Analyze Particles...", "size=0-Infinity exclude clear add");
if (roiManager("count") == 0) {
    print("Error: Failed to derive Apical_In region. Check mask subtraction.");
    exit();
}

// Assuming the first (and only) ROI is Apical_In
roiManager("Select", 0);
roiManager("Rename", "Apical_In");
roiManager("Measure");
apicalInArea = getResult("Area", nResults - 1);

// Close temporary mask images
selectImage(wholeCellMaskID);
run("Close");
selectImage(apicalOutMaskID);
run("Close");
selectImage(resultImageID);
run("Close");

// ------------------------------------------------
// 5. Calculate percentage ratios
// ------------------------------------------------
apicalOutRatio = (apicalOutArea / wholeCellArea) * 100;
apicalInRatio = (apicalInArea / wholeCellArea) * 100;

// Print results in the Log window
print("Whole cell area = " + wholeCellArea);
print("Apical-out area = " + apicalOutArea + " (" + apicalOutRatio + " %)");
print("Apical-in area  = " + apicalInArea + " (" + apicalInRatio + " %)");

// -------------------------------------------
// 6. Display in different colors
// -------------------------------------------
selectImage(originalImageID);
run("RGB Color"); // Convert to RGB to allow colored fill

// **Do NOT reset the ROI Manager here**
// roiManager("reset"); // <-- Remove or comment out this line

// Add "Apical_Out" ROI to ROI Manager (if not already present)
roiManager("Select", "Apical_Out");
roiManager("Add");

// Add "Apical_In" ROI to ROI Manager (if not already present)
roiManager("Select", "Apical_In");
roiManager("Add");

// Fill Apical_Out (red)
roiManager("Select", "Apical_Out");
setColor("red"); // Alternatively, setColor(255, 0, 0);
run("Fill", "slice");

// Fill Apical_In (green)
roiManager("Select", "Apical_In");
setColor("green"); // Alternatively, setColor(0, 255, 0);
run("Fill", "slice");

// -------------------------------------------
// End of script
// -------------------------------------------
print("Segmentation and analysis complete.");
