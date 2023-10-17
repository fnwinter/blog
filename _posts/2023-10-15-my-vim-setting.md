---
layout: post
title: "나의 vim setting"
author: "jungjik.lee"
categories: article
tags: [vim]
---

# 나의 vim setting

- [vim 설치](https://www.vim.org/)
- vim 설치 window
  - winget install -e --id vim.vim
- 우선 [번들 설치](https://github.com/VundleVim/Vundle.vim)

<pre><code>
"--- Basic vim settings ---
set nu 
set guifont=Liberation\Mono
set shiftwidth=2
set tabstop=2
set softtabstop=2
set expandtab
set ff=unix
set nobackup
set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [ASCII=\%03.3b]\ [HEX=\%02.2B]\ [POS=%04l,%04v][%p%%]\ [LEN=%L]
set laststatus=2
set autoindent
set smartindent
set hlsearch
set guioptions+=m
set clipboard=unnamedplus
set noswapfile
colorscheme desert
let NERDTreeShowHidden=1

"--- Auto commands setting ---
autocmd VimEnter * NERDTree
autocmd VimEnter * wincmd w
autocmd VimEnter * silent execute "!~/.vim/cp_rc.sh"
autocmd FileType python setl sw=2 sts=2 et

"--- Cscope settings ---
set csprg=/usr/bin/cscope
set csto=0
set cst
set nocsverb
set cscopequickfix=s-,c-,d-,i-,t-,e-,f-
set csverb
</code></pre>
