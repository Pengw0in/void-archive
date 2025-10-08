import os
import sys
import comtypes.client
from pptx import Presentation

def convert_pptx_to_pdf(input_file_path, output_file_path=None):
    """
    Convert a PowerPoint file (PPTX) to PDF
    
    Args:
        input_file_path (str): Path to the PowerPoint file
        output_file_path (str, optional): Path for the output PDF file. 
                                        If not provided, uses the same name with .pdf extension
    
    Returns:
        str: Path to the created PDF file
    """
    # Ensure input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # Get absolute paths
    input_file_path = os.path.abspath(input_file_path)
    
    # Create output file path if not provided
    if output_file_path is None:
        output_file_path = os.path.splitext(input_file_path)[0] + ".pdf"
    else:
        output_file_path = os.path.abspath(output_file_path)
    
    # Create PDF from PowerPoint
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = True
    
    try:
        deck = powerpoint.Presentations.Open(input_file_path, WithWindow=False)
        deck.SaveAs(output_file_path, 32)  # 32 is the PDF format code
        deck.Close()
        print(f"PDF created successfully: {output_file_path}")
    except Exception as e:
        raise Exception(f"Failed to convert PowerPoint to PDF: {str(e)}")
    finally:
        powerpoint.Quit()
    
    return output_file_path

def batch_convert_folder(folder_path, output_folder=None):
    """
    Convert all PPTX files in a folder to PDF
    
    Args:
        folder_path (str): Path to folder containing PPTX files
        output_folder (str, optional): Path to folder for PDF output. If not provided,
                                      PDFs will be created in the same folder as PPTX files
    """
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"Folder not found: {folder_path}")
    
    if output_folder and not os.path.isdir(output_folder):
        os.makedirs(output_folder)
    
    for file in os.listdir(folder_path):
        if file.lower().endswith('.pptx'):
            input_path = os.path.join(folder_path, file)
            
            if output_folder:
                output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.pdf')
            else:
                output_path = os.path.join(folder_path, os.path.splitext(file)[0] + '.pdf')
            
            try:
                convert_pptx_to_pdf(input_path, output_path)
                print(f"Converted: {file}")
            except Exception as e:
                print(f"Failed to convert {file}: {str(e)}")

if __name__ == "__main__":
    # Example usage for single file conversion
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        
        try:
            convert_pptx_to_pdf(input_file, output_file)
        except Exception as e:
            print(f"Error: {str(e)}")
            sys.exit(1)
    else:
        print("Usage: python pptx_to_pdf.py input.pptx [output.pdf]")
        print("Or to convert all PPTX files in a folder:")
        print("python pptx_to_pdf.py --batch input_folder [output_folder]")
        
        # Example of batch conversion
        # batch_convert_folder("path/to/pptx/files", "path/to/output/pdfs")