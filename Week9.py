# Week 9 HW

# Problem 5


easter_cake_recipe = """
Position a rack in the middle of the oven.
Preheat the oven to 350°F (176°C).
Grease two 9-inch round cake pans, line the bottom with parchment paper, and then grease the top.
Or grease and flour the bottom and sides of both pans.Whisk flour, baking soda, salt, and cinnamon in a medium bowl until very well blended.
In a separate bowl, whisk the oil, granulated sugar, brown sugar, and vanilla.
Add the eggs, one at a time, whisking after each one.
Switch to a large rubber spatula.
Scrape the sides and bottom of the bowl, then add the dry ingredients in three parts, gently stirring until they disappear and the batter is smooth.
Stir in the carrots, nuts, and raisins.Divide the cake batter between the prepared cake pans.
Bake until the tops of the cake layers are springy."""

import string

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct
            
def count_e(text):
    count = 0
    for c in text:
        if c == "e":
            count += 1
    return(count)

def analyze_text(easter_cake_recipe):
    text_nopunct = remove_punctuation(easter_cake_recipe)
    word_list = text_nopunct.split()
    total_words = len(word_list)
    words_with_e = count_e(easter_cake_recipe)
    percentage_with_e = (words_with_e / total_words) * 100
    s1 = "Your text contains {0} words, of which {1} ({2:.1f}%) contain an 'e'.".format(total_words, words_with_e, percentage_with_e)
    print(s1)

analyze_text(easter_cake_recipe)
