

------------------------- Exercise 1

doubles :: [Int] -> [Int]
doubles n = [2*x | x <- n]

odds :: [Int] -> [Int]
odds n = [m | m <- n , odd m]

doubleodds :: [Int] -> [Int]
doubleodds n = [2*m | m <- n , odd m]

shorts :: [String] -> [String]
shorts n = [m | m <- n, length m <= 5]

squarePositives :: [Int] -> [Int]
squarePositives n = [m^2 | m <- n, m > 0]

oddLengthSums :: [[Int]] -> [Int]
oddLengthSums n = [ sum m | m <- n, odd (length m)]

remove :: Eq a => [a] -> a -> [a]
remove n r = [ m | m <- n, m /= r]

removeAll :: Eq a => [a] -> [a] -> [a]
removeAll n r = [m | m <- n, m `notElem` r]

everyother :: [a] -> [a]
everyother n = [ m | (m, ms) <- zip n [1..], odd ms  ]

same :: Eq a => [a] -> [a] -> [Int]
same n ns = [mt | (m, ms, mt) <- zip3 n ns [1..], m == ms]

------------------------- Exercise 2

pairs :: [a] -> [b] -> [(a,b)]
pairs n m = [(x,y)| x <- n, y <- m]

selfpairs :: Ord a => [a] -> [(a,a)]
selfpairs n = [ (ma, mb) | ma <- n, mb <- n, mb >= ma]

pyts :: Int -> [(Int,Int,Int)]
pyts n = take n [(x,y,z) | x <- [1..n], y <- [1..n], z <- [1..n], x^2 + y^2 == z^2, x < y]

