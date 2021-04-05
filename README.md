# Non-binary Search Tree for UUID

## Introduction

Binary or non-binary search trees are node-based data structures and they're called search trees because they can be used to search for the presence of an element in `0(log(n))` time, in which `n` is the number of nodes in the tree.

The non-binary search tree here implemented has many benefits, among them:
1. It's an ideal way to represent the storing data with hierarchical way;
2. It reflects structural relationships that exist in the given dataset;
3. It makes insertion and deletion faster than linked lists and arrays;
4. It's a flexible way of holding and moving data;
5. It can be used to store as many nodes as possible;
6. It can be very useful when dealing with large batches of dynamic data.

To storage data, I've handled a universally unique identifier (UUID), a widely used unique representation (in contrast with an auto-generated integer unique key). UUIDs have the following advantages:
- They can be generated offline;
- They can make replication trivial (in contrast to integer unique keys);
- They are environment independent, which make them easier to manage in distribuited enviroments.

You can read more about UUIDs here: https://mareks-082.medium.com/auto-increment-keys-vs-uuid-a74d81f7476a

By using the version 4 of UUID, the first element of our key can be one of the following: a vowel, a consonant, an odd number or an even number. And that's how I've planned this non-binary tree representation.

### Algorithm complexity for non-binary search trees

#### Time complexity

| Operation | Best Case Complexity | Average Case Complexity | Worst Case Complexity |
| :---: | :---: | :---: | :---: | 
| Insertion | O(log n) | O(log n) | 0(n) |
| Search | O(log n) | O(log n) | O(n) |
| Deletion | O(log n) | O(log n) | 0(n) |

That means that searching, inserting and deleting can be done in logarithmic time, which present an excelent results according to  the Big-O Complexity Chart for algorithms.

![alt text](https://github.com/danielaczarref/NonBinarySearchTree/blob/master/BigOComplexityChart.png?raw=true)

You can read more about Big-O Complexity Charts over here: https://www.bigocheatsheet.com/

## How it works

In order to simplify additions to my non-binary search tree, I've generated 500 version 4 UUIDs (source: https://www.uuidgenerator.net/). And, since every UUID generated will start with either a vowel, a consonant, an odd number or an even number, I've decided to ramify my tree to support all 4 kinds of nodes.

Therefore, my non-binary search tree has 4 nodes: 
- Vowels node: it will storage all UUID starting with a vowel ["a", "e", "i", "o", "u"];
- Consonants node: it will storage all UUID starting with a non-digit element not in ["a", "e", "i", "o", "u"], which means, all consonants;
- Odds node: it will storage all UUID starting with an odd number;
- Evens node: it will storage all UUID starting with an even number.

The visual representation of my non-binary search tree for UUIDs can be seen in the following image.

![alt text](https://github.com/danielaczarref/NonBinarySearchTree/blob/master/NBST.png?raw=true)

So far, I've managed to implement the Class Node and the Class Tree, and in the last one I've implemented, so far, all the following functions:

- `getRoot`: it will return the tree's root element;
- `add` and `_add`: they will insert a new element according to its initial (vowel, consonant, odd number or even number);
- `valueType`: it will return the type of node the element will be inserted into (vowel, consonant, odd number or even number);
- `addFromFile`: given a filepath, it will add its content to the tree;
- `search` and `_search`: they will search a given element into each tree node;
- `order` and `_order`: they will order all elements in the following order: evens, odds, vowels and consonants;

## TO-DO
- `delete` and `_delete` functions.



