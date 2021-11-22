

ladies    = ["Mary","Kitty","Lydia","Elizabeth","Jane"]
gentlemen = ["Charles","Fitzwilliam","George","William"]

------------------------- Exercise 1

member :: [String] -> String -> Bool
member    []  _ = False
member (x:xs) y
    | x == y    = True
    | otherwise = member xs y

member' :: [String] -> String -> Bool
member'    []  _ = False  
member' (x:xs) y = (x==y) || (member' xs y)

remove :: [String] -> String -> [String]
remove [] _ = []
remove (x:xs) y
    | x /= y = x : remove xs y
    | otherwise = xs


------------------------- Exercise 2

members :: [String] -> [String] -> Bool
members xs    []  = True
members xs (y:ys)
    | member xs y = members xs ys
    | otherwise = False 

members' :: [String] -> [String] -> Bool
members' xs [] = True
members' xs (y:ys) = member xs y && members xs ys == True

removeAll :: [String] -> [String] -> [String]
removeAll xs [] = xs
removeAll xs (y:ys) = removeAll (remove xs y) ys


------------------------- Exercise 3

before :: [Char] -> [Char] -> Bool
before _ [] = True
before [] _ = False
before (x:xs) (y:ys)
    | x < y = True
    | x == y = before xs ys
    | otherwise = False

before' :: [Char] -> [Char] -> Bool
before' _ [] = True
before' [] _ = False
before' (x:xs) (y:ys) = x < y || x == y && before' xs ys
    

sorted :: [String] -> Bool
sorted [] = True
sorted [x] = True
sorted (x:(xs:(xt)))
    | before x xs = sorted (xs:(xt))
    | otherwise = False