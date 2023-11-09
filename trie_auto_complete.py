class Node:
    def __init__(self, data=None):
        """
        Init for the Node class

        Input:
            data: the data to be stored in the node
        Return:
            None

        Time complexity: O(1)
        Aux space complexity: O(1)
        """
        # the children of the node(constant size of 27)
        self.links = [None for _ in range(27)]
        # the sentence stored in the node
        self.data = data
        # frequency of the sentence but only add in the terminal node
        self.count = 0

class CatsTrie:
    def __init__(self, sentences):
        """
        Init for the CatsTrie class

        Input:
            sentences: the list of sentences to be inserted into the trie
        Return:
            None

        Time complexity: O(NM) where N is the number of sentences and M is the number of characters in the longest sentence

        Aux space complexity: O(1)

        Space complexity: O(NM) where N is the number of sentences and M is the number of characters in the longest sentence
        """
        # root node
        self.root = Node()
        # loop through the sentences list which gives O(N) time complexity and insert each sentence which is
        # M number of characters gives O(M) time complexity
        for sentence in sentences:
            self.insert(sentence, sentence)

    def insert(self, key, data):
        """
        Insert the sentence in the trie and also add the whole sentence in the terminal node.data and
        when the sentence is already in the trie, increment by 1 as frequency in the terminal node.count

        Input:
            key: the sentence to be inserted
            data: the data(whole sentence) to be stored in the terminal node
        Return:
            None

        Time complexity: O(M) where M is the number of characters in the word
        Aux space complexity: O(1)

        """
        current = self.root
        # O(M) time complexity
        for char in key:
            # $ = 0, a = 1
            index = ord(char) - 97 + 1
            if current.links[index] is not None:
                current = current.links[index]
            else:
                current.links[index] = Node()
                current = current.links[index]
        # add the whole sentence in the terminal node.data
        index = 0
        if current.links[index] is not None:
            current = current.links[index]
        else:
            current.links[index] = Node(data)
            current = current.links[index]
        # if the word is already in the trie, increment the count in terminal node
        current.count += 1


    def autoComplete(self, prompt):
        """
        Return the most frequent sentence that starts with the prompt. However, when there is no such sentence,
        return None, so this will return with time complexity O(X) and O(1) aux space complexity only. Thus, it is
        an output-sensitive complexity.

        Input:
             prompt: the prompt to be searched
        Return:
            the most frequent sentence that starts with the prompt

        Time complexity: O(X+Y) where X is the length of the prompt and
                                Y is the length of the most frequent sentence that starts with the prompt

        Aux space complexity: O(Y) where Y is the length of the most frequent sentence that starts with the prompt

        Space complexity: O(X+Y) where X is the length of the prompt(input) and
                                 Y is the length of the most frequent sentence that starts with the prompt(aux)
        """

        current = self.root
        checker = 0  # used to check if the last character of prompt has any children
        # O(X) time complexity
        for char in prompt:
            # $ = 0, a = 1
            index = ord(char) - 97 + 1
            if current.links[index] is not None:
                current = current.links[index]
            else:
                return None
        # constant loop of 27 which gives O(1) time complexity
        # check if the last character of prompt has any children and if not, return None
        for i in range(27):
            if current.links[i] is not None:
                checker = 1
                break
        if checker == 1:
            res = []
            # O(Y) time complexity and aux space complexity
            self.autoComplete_aux(current, res)
            return res[0][0]
        else:
            return None



    def autoComplete_aux(self, current, res):
        """
        Check the children of the prompt and append the most frequent sentence that starts with prompt with
        the highest frequency(count) in form of (sentence,frequency) in res

        Input:
            current: the current node
            res: the most frequent sentence that starts with the prompt, frequency of the sentence

        Time Complexity: O(Y) where Y is the length of the most frequent sentence that starts with the prompt
        Aux space complexity: O(Y) where Y is the length of the most frequent sentence that starts with the prompt

        """
        # base case
        # when the current node is a terminal node
        if current.data is not None:
            # check if the frequency of sentences is bigger than the one in res, if so, pop it and append the new one
            # O(Y) time complexity and aux space complexity, appending Y length of sentence and its frequency into res
            if len(res) != 0 and current.count > res[0][1]:
                res.pop()
                res.append((current.data, current.count))
            # the res is still empty so just append it
            elif len(res) == 0:
                res.append((current.data, current.count))
            # to break
            return res
        # constant loop through the children of the current node which gives O(1) time complexity
        for child in range(27):
            if current.links[child] is not None:
                self.autoComplete_aux(current.links[child], res)