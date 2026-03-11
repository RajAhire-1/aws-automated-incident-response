@echo off
echo Adding all changes...
git add .

echo.
echo Committing changes...
git commit -m "Update project files"

echo.
echo Pushing to remote repository...
git push origin main

echo.
echo Done!
pause
