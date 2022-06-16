<H1>Hi, this is the code to convert HEIC files to PNG<H1>

This code will convert HEIC files to PNG, and it supports multiple files at once, keeping its original name.

<H2> Steps:</H2>

<ol>

  <li><h3>1:  First drop the HEIC files a folder, and declare it on the <h3></li>  
  <li>
    <H3>2:  Declare the base Directory (With the .HEIC files)<h3>
    It can be declared in this variable 

 ``` base_dir = os.listdir('./folder_name/') ```

 changing the 'folder_name' to the name of the folder
 ***Remind to keep the "./" at the beginning, and the "/" at the end***
  </li>
  <li>
    <h3>2:    Declare the output directory for the .PNG files</h3>
    It can be declared in this variable 

``` output_dir = os.path.join('./png_files/') ```
 changing the 'folder_name' to the name of the folder
 ***Remind to keep the "./" at the beginning, and the "/" at the end***
  </li>
  <li>

 ***Run the code and watch the magic happens*** 
  </li>
</ol>