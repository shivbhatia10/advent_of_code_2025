import Control.Monad
import System.IO

processLine :: (Int, Int) -> String -> IO (Int, Int)
processLine (curr, password) line = do
  let operation = head line
      value = read (tail line) :: Int
      (newCurr, newPassword) =
        if operation == 'R'
          then
            let newVal = curr + value
                addPassword = newVal `div` 100
                newCurrVal = newVal `mod` 100
             in (newCurrVal, password + addPassword)
          else
            let newVal = curr - value
                addPassword =
                  if newVal <= 0
                    then (if curr /= 0 then 1 else 0) + ((-newVal) `div` 100)
                    else 0
                newCurrVal = newVal `mod` 100
             in (newCurrVal, password + addPassword)

  putStrLn $ show newCurr ++ " " ++ show newPassword ++ " " ++ line
  return (newCurr, newPassword)

main :: IO ()
main = do
  contents <- readFile "input.txt"
  let linesOfFile = lines contents
  (_, finalPassword) <- foldM processLine (50, 0) linesOfFile
  print finalPassword
