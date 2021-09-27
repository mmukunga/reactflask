# reactflask
# Tutorial: https://gist.github.com/Reine0017
cd D:\Temps\ReactFlask\frontend
npm run build
cd D:\Temps\ReactFlask
git status
git add .
git commit -m "first commit"
# git commit --allow-empty -m "Purge cache"
git branch -M main
git push -u origin main

heroku logs --tail --app reactflask-smb

heroku builds:cache:purge -a reactflask  --confirm reactflask-smb
