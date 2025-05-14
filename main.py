import sys
from stats import get_book_text, get_num_words, count_characters, final_sort

def main():
    # Check if the correct number of arguments was provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command-line arguments
    book_path = sys.argv[1]
    
    # Use the provided book path instead of hard-coding it
    frankenstein_txt = get_book_text(book_path)
    word_count = get_num_words(frankenstein_txt)
    character_count = count_characters(frankenstein_txt)
    sorted_characters = final_sort(character_count)

    print("============ BOOKBOT ============")   
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

main()