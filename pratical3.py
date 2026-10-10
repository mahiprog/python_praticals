#program1 :Sequence operations
def main():
    seq = [10, 20, 30, 40, 50]

    print("Original sequence:", seq)
    print("First element:", seq[0])
    print("Last element:", seq[-1])
    print("Sliced (1:4):", seq[1:4])
    print("Is 30 in sequence?", 30 in seq)
    print("Length:", len(seq))
    print("Maximum:", max(seq))
    print("Minimum:", min(seq))


if __name__ == "__main__":
    main()

#program2 :List methods
def main():
    fruits = ["apple", "banana", "cherry"]
    print("Original list:", fruits)

    fruits.append("orange")
    print("After append:", fruits)

    fruits.insert(1, "mango")
    print("After insert:", fruits)

    fruits.remove("banana")
    print("After removing banana:", fruits)

    fruits.pop()
    print("After popping last element:", fruits)

    fruits.sort()
    print("After sort:", fruits)

    fruits.reverse()
    print("After reverse:", fruits)

    print("Index of mango:", fruits.index("mango"))
    print("Count of apple:", fruits.count("apple"))


if __name__ == "__main__":
    main()

#program3 :Tuple methods
def main():
    tup = (1, 2, 3, 2, 4, 2)

    print("Tuple:", tup)
    print("Count of 2:", tup.count(2))
    print("Index of 4:", tup.index(4))


if __name__ == "__main__":
    main()

#program4 :String methods
def main():
    text = "Hello World"

    print("Original text:", text)
    print("Lowercase:", text.lower())
    print("Uppercase:", text.upper())
    print("Replace:", text.replace("World", "Python"))
    print("Find World:", text.find("World"))
    print("Split:", text.split())
    print("Starts with H:", text.startswith("H"))
    print("Ends with d:", text.endswith("d"))


if __name__ == "__main__":
    main()

#program5 :Built-in Functions on Sequences
def main():
    names = ['Alice', 'Bob', 'Charlie']
    scores = [85, 90, 78]

    print("Using enumerate:")
    for i, name in enumerate(names):
        print(f"{i}: {name}")

    print("\nUsing zip:")
    for name, score in zip(names, scores):
        print(f"{name} scored {score}")

    print("\nReversed names:", list(reversed(names)))
    print("Sorted scores:", sorted(scores))


if __name__ == "__main__":
    main()