#!/usr/bin/env runghc

import Data.Char(digitToInt)

cnv :: String -> [Int]
cnv [] = []
cnv (x:xs) = digitToInt x : cnv xs

binToInt :: [Int] -> Int
binToInt = foldl (\acc x -> x + 2 * acc) 0

part1 :: [[Int]] -> Int
part1 x =
  let 
    gamma = map (\a -> if a > div (length x) 2 then 1 else 0) (foldr1 (zipWith (+)) x)
    epsilon = map (\a -> if a == 0 then 1 else 0) gamma
  in binToInt gamma * binToInt epsilon

part2 :: (Int -> Int -> Bool) -> Int -> [[Int]] -> [[Int]]
part2 p i xs
  | i >=  length (head xs) = xs
  | length xs == 1 = xs
  | otherwise = part2 p (i + 1) xs'
  where
    xs' = filter (\a -> a !! i == keepBit) xs
    keepBit = if ones `p` zeroes then 1 else 0
    (ones, zeroes) = colCount $ map (!! i) xs

colCount :: [Int] -> (Int, Int)
colCount xs = foldr (\a (o, z) -> if a == 1 then (o + 1, z) else (o, z + 1)) (0, 0) xs

main :: IO ()
main = do
  s <- readFile "input.txt"
  let input = map cnv $ lines s
  
  print $ part1 input
  
  let oxygen = binToInt $ head $ part2 (>=) 0 input
  let scrubber = binToInt $ head $ part2 (<) 0 input
  print $ oxygen * scrubber
