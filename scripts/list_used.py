

if __name__ == "__main__":

    # Empty occurence
    names = list()
    for name in ["Shivam", "Jalotra"]:
        names.append(name)  
    print(names)

    names_new = list(('Shivam', 'Jalotra'))
    
    # Assertion (the values should always be same) 
    assert names_new == names    