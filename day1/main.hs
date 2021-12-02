#!/usr/bin/env runghc

part1 :: [Int] -> Int
part1 (x1:x2:xs)
  | null xs = if x1 < x2 then 1 else 0
  | x1 < x2 = 1 + part1 (x2:xs)
  | otherwise = 0 + part1 (x2:xs)

sumThree :: [Int] -> [Int]
sumThree [] = []
sumThree xs = s : sumThree next
  where
    s = sum (take 3 xs)
    next = tail xs

--part2 :: [Int] -> Int
--part2 (x:xs)
--  | length xs < 3 = 0
--  | x < xs !! 2 = 1 + part2 xs
--  | otherwise = part2 xs

main :: IO ()
main = do
  s <- readFile "input.txt"
  let nums = map read $ lines s

  print $ part1 nums
  print $ part1 $ sumThree nums

  --print $ part2 nums
