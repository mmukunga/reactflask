
#!/bin/bash
echo "Hello, World!" 
cd D:\Temps\ReactFlask\frontend
echo rmdir 'D:\Temps\ReactFlask\frontend\build\'  /s /q
remove-item 'D:\Temps\ReactFlask\frontend\build\*' -recurse -force
npm run build
cd D:\Temps\ReactFlask

git status
git add .
git commit -m "first commit"
echo git commit --allow-empty -m "Purge cache"
git branch -M main
git push -u origin main
echo "Knowledge is power."