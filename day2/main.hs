#!/usr/bin/env runghc

cnv :: [String] -> (String, Int)
cnv (dir:len:tail) = (dir, read len)

part1 :: [(String, Int)] -> (Int, Int) -> Int
part1 [] (x, y) = x * y
part1 ((dir, len):tail) (x, y)
  | dir == "forward" = part1 tail (x + len, y)
  | dir == "down" = part1 tail (x, y + len)
  | dir == "up" = part1 tail (x, y - len)
  | otherwise = error "undefined direction"

part2 :: [(String, Int)] -> (Int, Int, Int) -> Int
part2 [] (x, y, aim) = x * y
part2 ((dir, len):tail) (x, y, aim)
  | dir == "forward" = part2 tail (x + len, y + (aim * len), aim)
  | dir == "down" = part2 tail (x, y, aim + len)
  | dir == "up" = part2 tail (x, y, aim - len)
  | otherwise = error "undefined direction"

main :: IO ()
main = do
  s <- readFile "input.txt"
  let input = map cnv $ map words $ lines s

  print $ part1 input (0, 0)
  print $ part2 input (0, 0, 0)
