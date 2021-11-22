 

ladies    = ["Mary","Kitty","Lydia","Elizabeth","Jane"]
gentlemen = ["Charles","Fitzwilliam","George","William"]
couples   = [("Elizabeth","Fitzwilliam"),("Charlotte","William"),("Lydia","George"),("Jane","Charles")]

------------------------- Exercise 1

ditch :: Int -> [a] -> [a]
ditch _ []     = []
ditch 0 (x:xs) = x:xs
ditch n (x:xs) = ditch (n-1) xs


at :: [a] -> Int -> a
at (x:xs) 0 = x
at (x:xs) n
  | n > 0 && n < length(x:xs) = at xs (n-1)
  | otherwise = error "negative, equal or greater then length input"


------------------------- Exercise 2

find :: Eq a => a -> [(a,b)] -> b
find n ((a,b):xs)
  | n == a = b
  | n /= a = find n xs
  | otherwise = error "unpaiared element"

which :: Eq a => a -> [a] -> Int
which a [] = error "list is empty"
which a (x:xs) = aux 0 a (x:xs)
  where
    aux :: Eq a => Int -> a -> [a] -> Int
    aux m n [] = error "list is empty"
    aux m n (x:xs)
      | n == x = m
      | otherwise = aux (m+1) n (xs)

member :: Eq a => [a] -> a -> Bool
member [] _ = False
member (x:xs) y
  | x == y = True
  | otherwise = member xs y

remove :: Eq a => [a] -> a -> [a]
remove [] _ = []
remove (x:xs) y
    | x /= y = x : remove xs y
    | otherwise = xs
    
before :: Ord a => [a] -> [a] -> Bool
before _ [] = True
before [] _ = False
before (x:xs) (y:ys)
    | x < y = True
    | x == y = before xs ys
    | otherwise = False


sorted :: Ord a => [a] -> Bool
sorted [] = True
sorted [x] = True
sorted (x:(xs:xt))
  | before [x] [xs] = sorted (xs:(xt))
  | otherwise = False

------------------------- Exercise 3

merge :: Ord a => [a] -> [a] -> [a]
merge xs [] = xs
merge [] ys = ys
merge (x:xs) (y:ys)
  | x < y = x : merge xs (y:ys)
  | x > y = y : merge (x:xs) ys
  | x == y = x : merge xs ys
  | otherwise =  error "Woops, you've broken it!"


minus :: Ord a => [a] -> [a] -> [a]
minus xs [] = xs
minus [] ys = []
minus xs (y:ys)
  | member xs y = minus (remove xs y) (ys)
  | otherwise = minus xs ys

    
msort :: Ord a => [a] -> [a]
msort []  = []
msort [xs] = [xs]
msort  xs = merge (msort ys) (msort zs)
            where 
              ys = take (length xs `div` 2) xs
              zs = drop (length xs `div` 2) xs