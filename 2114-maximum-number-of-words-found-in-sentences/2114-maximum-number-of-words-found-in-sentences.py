class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        count_most_words=0
        for sentence in sentences:
            list_of_words=sentence.split(" ")
            num_of_words=len(list_of_words)
            count_most_words=max(count_most_words, num_of_words)
        return count_most_words
        