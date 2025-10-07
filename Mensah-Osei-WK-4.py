'''
'''


import re
import csv
import os


from prettytable import PrettyTable  # pip install prettytable

print("\nMensah-Osei-WK-4\n")


urlPattern = re.compile(
    b'\\w+:\\/\\/[\\w@][\\w.:@]+\\/?[\\w\\.?=%&=\\-@/$,]*'
)


CHUNK_SIZE = 65535  # 65,535 bytes


def process_file(file_path):
    """
    
    """
    urlDict = {}
    if not os.path.isfile(file_path):
        print(f"\nERROR: File not found: {file_path}")
        return urlDict

    try:
        with open(file_path, 'rb') as targetFile:
            overlap = b''
            chunk_count = 0

            while True:
                fileChunk = targetFile.read(CHUNK_SIZE)
                if not fileChunk:
                    break

                chunk_count += 1
                print(f"Processing chunk #{chunk_count}")

                # Combine them
                fileChunk = overlap + fileChunk

                # Find the matches
                urlMatches = urlPattern.findall(fileChunk)

                for eachUrl in urlMatches:
                    try:
                        eachUrl = eachUrl.decode("utf-8", errors='ignore')
                        urlDict[eachUrl] = urlDict.get(eachUrl, 0) + 1
                    except Exception as decode_err:
                        print(f"Decode error: {decode_err}")

                # Save the last 20 bytes 
                overlap = fileChunk[-20:]

    except Exception as err:
        print(f"File processing error: {err}")

    return urlDict


def display_results(urlDict):
    """
    
    """
    tblURL = PrettyTable(["URL", "Occurrences"])
    for url, cnt in urlDict.items():
        tblURL.add_row([url, cnt])

    tblURL.align = 'l'
    tblURL.title = "Sorted URL Results"
    print("\nGenerating Sorted Result Table:\n")
    print(tblURL.get_string(sortby="Occurrences", reversesort=True))

    return tblURL


def save_html_table(table, filename="Result.html"):
    """
    
    """
    try:
        html = table.get_html_string(sortby="Occurrences", reversesort=True)
        with open(filename, 'w', encoding='utf-8') as output:
            output.write(html)
        print(f"\nHTML table saved as '{filename}'")
    except Exception as err:
        print(f"Error writing HTML: {err}")


def save_csv(urlDict, filename="Result.csv"):
    """
    
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["URL", "Occurrences"])
            for url, count in urlDict.items():
                writer.writerow([url, count])
        print(f"CSV file saved as '{filename}'")
    except Exception as err:
        print(f"Error writing CSV: {err}")


def main():
    file_path = r"C:\Users\oseim\Downloads\mem.raw"  # Update it

    url_counts = process_file(file_path)

    if not url_counts:
        print("\nNo URLs found or file could not be read.")
        return

    #Display table in console
    table = display_results(url_counts)

    

    print("\nScript Complete")


if __name__ == "__main__":
    main()
