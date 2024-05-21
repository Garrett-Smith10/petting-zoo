# import the python datetime module to help us create a timestamp


from walking import Llama, Cow, Bear, Lion, Panther
from swimming import Dolphin, Shark, GoldFish, Whale, Guppy
from slithering import Snake, Slug, Bigger_Snake, Small_Snake, Snail





































miss_fuzz = Llama("Miss Fuzz", "domestic llama")
 

miss_fuzzy = Cow("Miss Fuzzy", "domestic cow")

 
miss_claw = Lion("Miss Claw", "domestic lion")


miss_fuzzier = Bear("Miss Fuzzier", "domestic bear")
 

miss_scratch = Panther("Miss Scratch", "domestic panther")



miss_scales = Snake("Miss Scales", "domestic snake")


miss_slime = Slug("Miss Slime", "domestic slug")


miss_big = Bigger_Snake("Miss Big", "domestic bigger snake")


miss_small = Small_Snake("Miss Small", "domestic small snake")


miss_slow = Snail("Miss Slow", "domestic snail")



miss_ocean = Dolphin("Miss Ocean", "domestic dolphin")


miss_tooth = Shark("Miss Tooth", "domestic shark")


miss_hump = Whale("Miss Hump", "domestic whale")


miss_gold = GoldFish("Miss Gold", "domestic goldfish")


miss_gup = Guppy("Miss Gup", "domestic guppy")





for key, value in vars(miss_fuzz).items():
    print(f"{key}: {value}")

    print(miss_fuzz.name)