
------------------------- Exercise 1

doubles :: [Int] -> [Int]
doubles [] = []
doubles (x:xs) = 2*x : doubles (xs)

doublesMap :: [Int] -> [Int]
doublesMap = map (*2)

odds :: [Int] -> [Int]
odds [] = []
odds (x:xs)
    | (odd x) = x : odds xs
    | otherwise = odds xs

oddsMap :: [Int] -> [Int]
oddsMap = filter odd


doubleodds :: [Int] -> [Int]
doubleodds [] = []
doubleodds xs =  doubles (odds xs)

doublesoddsHoF :: [Int] -> [Int]
doublesoddsHoF xs = doublesMap (oddsMap xs)


------------------------- Exercise 2

shorts :: [String] -> [String]
shorts [] = []
shorts (x:xs) 
    | lenFive x = x : shorts xs
    | otherwise = shorts xs
    where 
    lenFive [] = False
    lenFive y
        | length (y) <= 5 = True
        | otherwise = False


squarePositives :: [Int] -> [Int]
squarePositives [] = []
squarePositives ys = map (^2) (filter posInts ys)
    where
    posInts x
        | x > 0 = True
        | otherwise = False
        


oddLengthSums :: [[Int]] -> [Int]
oddLengthSums x = map (sum) (filterList x)


filterList :: [[Int]] ->[[Int]]
filterList [] = []
filterList (x:xs)
    | odd (length x) = x : filterList xs
    | otherwise = filterList xs


------------------------- Exercise 3

remove :: Eq a => [a] -> a -> [a]
remove x y  = filter (\x -> x/= y) x

numbered :: [a] -> [(Int,a)]
numbered [] = []
numbered x = zip [1 .. length x] x

everyother :: [a] -> [a]
everyother [] = []
everyother x = map snd(filterPair (numbered x))
    where
        filterPair :: [(Int,b)] -> [(Int,b)]
        filterPair [] = []
        filterPair ((x,xs) : rest)
            | odd x = (x,xs) : filterPair (rest)
            | otherwise = filterPair rest

same :: Eq b => [b] -> [b] -> [Int]
same x y = map fst ( samePair (numbered x) (numbered y))
    where 
        samePair [] _ = []
        samePair _ [] = []
        samePair (x:xs) ys
            | x `elem` ys = x : samePair xs ys
            | otherwise = samePair xs ys
