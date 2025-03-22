class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

    def __repr__(self):
        return str(self.arr)


def expected_result():
    return [
        ("March 6", 120),
        ("March 7", 130),
        ("March 8", 140),
    ]

def test_hash_table():
    ht = HashTable()
    ht["March 6"] = 120
    ht["March 7"] = 130
    ht["March 8"] = 140

    assert ht["March 6"] == 120
    assert ht["March 7"] == 130
    assert ht["March 8"] == 140

    del ht["March 7"]
    try:
        _ = ht["March 7"]  # Should raise KeyError
        assert False  # This line should not be reached
    except KeyError:
        pass  # Correct behavior

    print("Hash Table Tests Passed!")


def main(test_key=None, test_value=None):
    ht = HashTable()
    
    # Insert predefined values
    ht["March 6"] = 120
    ht["March 7"] = 130
    ht["March 8"] = 140

    # ✅ Introduce branching based on test_key and test_value
    if test_key is not None and isinstance(test_key, str):
        ht[test_key] = test_value
        print(f"Inserted: {test_key} -> {test_value}")

    if test_key in ["March 6", "March 7", "March 8"]:
        retrieved_value = ht[test_key]
        print(f"Retrieved Value: {retrieved_value}")

    if test_key == "March 7":
        del ht[test_key]
        print(f"Deleted {test_key}")

    print(ht)
    
def expected_result():
    return [[('March 6', 120)], [('March 8', 140)]]

if __name__ == "__main__":
    main()

    
    






