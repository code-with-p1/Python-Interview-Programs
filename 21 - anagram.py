def are_anagrams(str1, str2):
  return sorted(str1) == sorted(str2)

result = are_anagrams("abcd", "acbd")
print(result)
print("****************************************")


def are_anagrams_dict(str1, str2):

  if len(str1) != len(str2):
    return False

  count = {}
  for char in str1:
    count[char] = count.get(char, 0) + 1
  
  for char in str2:
    if char not in count:
      return False

    print(count)

    count[char] = count[char] - 1

    if count[char] == 0:
      del count[char]
  
  print(count)
  return not count

result = are_anagrams_dict("angell", "lgeanl")
print(result)
print("****************************************")


def are_anagrams_counter(str1, str2):
  from collections import Counter
  return Counter(str1) == Counter(str2)

result = are_anagrams_counter("abcd", "acbd")
print(result)
print("****************************************")


def are_anagrams_sorted(str1, str2):
  return ''.join(sorted(str1)) == ''.join(sorted(str2))

result = are_anagrams_sorted("abcd", "acbd")
print(result)
print("****************************************")



def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    string_1 = str1.replace(" ", "").lower()
    string_2 = str2.replace(" ", "").lower()
    
    # If lengths are different, they can't be anagrams
    if len(string_1) != len(string_2):
        return False
    
    # Create a dictionary to count character frequencies
    first_string_char_count = {}
    
    # Count characters in first string
    for char in string_1:
        if char in first_string_char_count:
            first_string_char_count[char] += 1
        else:
            first_string_char_count[char] = 1
    
    print(f"Char Count of first String : {first_string_char_count}")

    # Subtract counts using second string
    for char in string_2:
        if char in first_string_char_count:
            first_string_char_count[char] -= 1
        else:
            # Character not found in first string
            print("HEre")
            return False

    print(first_string_char_count.values())
    
    # Check if all counts are zero
    for count in first_string_char_count.values():
        if count != 0:
            return False
    
    return True

# Example usage
string1 = "Aangell"
string2 = "lgeanlB"
print(f"Are '{string1}' and '{string2}' anagrams? {are_anagrams(string1, string2)}")