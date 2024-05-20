import os

class UniqueInt:
    @staticmethod
    def process_file(input_file_path, output_file_path):
        """
        Process the input file to find unique integers and write them to the output file in sorted order.
        
        Args:
            input_file_path (str): Path to the input file.
            output_file_path (str): Path to the output file.
        """
        # Use a set to store unique integers
        unique_integers = set()
        
        # Open the input file and read line by line
        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                try:
                    # Strip leading/trailing whitespace from the line
                    stripped_line = line.strip()
                    
                    # Skip empty lines
                    if stripped_line == '':
                        continue
                    
                    # Split the line into parts (words)
                    parts = stripped_line.split()
                    
                    # Skip lines with more than one part (more than one integer or invalid format)
                    if len(parts) != 1:
                        continue
                    
                    # Convert the part to an integer
                    number = int(parts[0])
                    
                    # Add the number to the set if it's within the valid range
                    if -1023 <= number <= 1023:
                        unique_integers.add(number)
                    
                except ValueError:
                    # Skip lines that cannot be converted to an integer
                    continue
        
        # Sort the unique integers
        sorted_integers = sorted(unique_integers)
        
        # Write the sorted unique integers to the output file
        with open(output_file_path, 'w') as output_file:
            for number in sorted_integers:
                output_file.write(f"{number}\n")

if __name__ == "__main__":
    # Define the directories for sample inputs and sample results
    sample_inputs_dir = '/dsa/hw01/sample_inputs'
    sample_results_dir = '/dsa/hw01/sample_results'

    # Process each input file in the sample inputs directory
    for input_filename in os.listdir(sample_inputs_dir):
        # Define the full path for the input file
        input_filepath = os.path.join(sample_inputs_dir, input_filename)
        
        # Define the full path for the output file
        output_filename = f"{input_filename}_results.txt"
        output_filepath = os.path.join(sample_results_dir, output_filename)
        
        # Process the input file and generate the output file
        UniqueInt.process_file(input_filepath, output_filepath)
        print(f"Processed {input_filepath} -> {output_filepath}")
