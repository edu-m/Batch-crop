@echo off
setlocal ENABLEDELAYEDEXPANSION
set/a fileNum = 1

for %%f in (*.png) do (
  REM problematic with name files that have spaces
  ren %%~nf%%~xf !fileNum!%%~xf 
  set/a fileNum += 1
)
