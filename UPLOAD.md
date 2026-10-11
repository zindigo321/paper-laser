# 上传公开版知识库

目标：[zindigo321/paper-laser](https://github.com/zindigo321/paper-laser)，分支 `main`。用户已明确选择 Public，无需更改仓库可见性。

## 文件范围

公开版包含 7 篇阅读笔记、7 份单篇 BibTeX、总览、对比及 4 篇许可允许的原始 PDF。另 3 篇只有来源说明，原因见 [PDF_LICENSES.md](PDF_LICENSES.md)。使用公开版压缩包 `paper-laser-public.zip`；旧的 `paper-laser-knowledge-base.zip` 含未获公开许可的全文，不应用于本公开仓库。

## 使用 GitHub Desktop

1. 从 [GitHub Desktop 官网](https://desktop.github.com/download/) 安装并登录。
2. 选择 File → Clone Repository → URL，填入 `https://github.com/zindigo321/paper-laser.git`，克隆到与解压目录不同的位置。
3. 选择 Repository → Show in Explorer（Mac 为 Show in Finder），打开刚克隆的目录。将公开版解压文件夹内部的全部内容复制进去，包括 `.gitattributes`；保留克隆目录的 `.git`。Mac 可用 `⌘ + Shift + .` 显示点号开头文件。
4. 确认当前分支 main，查看 Changes，选中本次知识库文件，填写 Summary：`docs: publish seven LiDAR paper notes and licensed PDFs`，点击 Commit。
5. 点击 Push origin；若提示远端新提交，先 Fetch/Pull 并合并，不强制推送。
6. 刷新仓库首页，确认 7 个论文目录、4 个 PDF、全部笔记及引用；点击 README 的 PDF、笔记和来源说明链接，查看公式、表格及 Mermaid。大 PDF 未出现预览时使用下载按钮核对。

## 在终端上传

先克隆已有仓库并复制公开版内容，保留历史和 `.git`；不要在 URL、文件或提交中写入令牌。

```bash
git clone https://github.com/zindigo321/paper-laser.git paper-laser-upload
cd paper-laser-upload
# 在此将解压的公开版文件内容复制到当前目录
python3 tools/verify_repository.py
git diff --check
git add README.md comparison.md references.bib source_manifest.json checksums.sha256 verification.md UPLOAD.md PDF_LICENSES.md .gitattributes papers tools
git commit -m "docs: publish seven LiDAR paper notes and licensed PDFs"
git pull --rebase origin main
git push origin main
```

## GitHub 连接授权

当前连接的 PDF 和 Markdown 上传接口均返回 HTTP 403 `Resource not accessible by integration`；可读取仓库不能证明具备写入权限。需要给当前 GitHub 连接配置访问本仓库的写入授权，或使用自己已经登录的 GitHub Desktop 完成上述上传。无需发送访问令牌。最新远端状态见 [verification.md](verification.md)。
