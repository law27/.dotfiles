set tabstop=4       " The width of a TAB is set to 4.
                    " Still it is a \t. It is just that
                    " Vim will interpret it to be having
                    " a width of 4.

set shiftwidth=4    " Indents will have a width of 4

set softtabstop=4   " Sets the number of columns for a TAB

set expandtab       " Expand TABs to spaces

set nocompatible

set rnu
set number
filetype plugin on
let java_highlight_functions = 1
let java_highlight_all = 1

" Specify a directory for plugins
" - For Neovim: stdpath('data') . '/plugged'
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')

" Make sure you use single quotes

" Shorthand notation; fetches https://github.com/junegunn/vim-easy-align
Plug 'lifepillar/vim-solarized8'
Plug 'junegunn/vim-easy-align'
Plug 'udalov/kotlin-vim'
Plug 'MarcWeber/vim-addon-mw-utils'
Plug 'tomtom/tlib_vim'
Plug 'garbas/vim-snipmate'
Plug 'honza/vim-snippets'
" Any valid git URL is allowed
Plug 'https://github.com/junegunn/vim-github-dashboard.git'

" Multiple Plug commands can be written in a single line using | separators

" On-demand loading
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'tpope/vim-fireplace', { 'for': 'clojure' }
Plug 'gruvbox-community/gruvbox'
Plug 'ryanoasis/vim-devicons'
Plug 'altercation/vim-colors-solarized'
Plug 'reedes/vim-colors-pencil'
Plug 'rakr/vim-colors-rakr'
Plug 'noahfrederick/vim-hemisu'
Plug 'neovimhaskell/haskell-vim'
Plug 'wesgibbs/vim-irblack'
Plug 'arcticicestudio/nord-vim'
Plug 'pangloss/vim-javascript'
Plug 'MaxMEllon/vim-jsx-pretty'
Plug 'neoclide/coc.nvim'
Plug 'prettier/vim-prettier', { 'do': 'yarn install' }


if has('nvim')
  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
else
  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif
" Using a non-master branch

" Using a tagged release; wildcard allowed (requires git 1.9.2 or above)

" Plugin options

" Plugin outside ~/.vim/plugged with post-update hook

" Unmanaged plugin (manually installed and updated)

" Initialize plugin system
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'NLKNguyen/papercolor-theme'
call plug#end()
let g:solarized_termcolors=256
set background=dark
colorscheme gruvbox
source ~/.vim/plugged/vim-snipmate/plugin/snipMate.vim

let &t_SI = "\e[5 q"
let &t_EI = "\e[2 q"

set timeoutlen=1000 ttimeoutlen=0

let g:haskell_enable_quantification = 1   " to enable highlighting of `forall`
let g:haskell_enable_recursivedo = 1      " to enable highlighting of `mdo` and `rec`
let g:haskell_enable_arrowsyntax = 1      " to enable highlighting of `proc`
let g:haskell_enable_pattern_synonyms = 1 " to enable highlighting of `pattern`
let g:haskell_enable_typeroles = 1        " to enable highlighting of type roles
let g:haskell_enable_static_pointers = 1  " to enable highlighting of `static`
let g:haskell_backpack = 1                " to enable highlighting of backpack keywords
let g:haskell_indent_if = 3
let g:haskell_indent_case = 2
let g:haskell_indent_let = 4
let g:haskell_indent_where = 6
let g:haskell_indent_before_where = 2
let g:haskell_indent_after_bare_where = 2
let g:haskell_indent_do = 3
let g:haskell_indent_in = 1
let g:haskell_indent_guard = 2
let g:haskell_indent_case_alternative = 1
let g:cabal_indent_section = 2

if exists("g:loaded_webdevicons")
  call webdevicons#refresh()
endif

nmap <F6> :NERDTreeToggle<CR>

let g:neovide_refresh_rate=140
set clipboard=unnamed


function! GuiTabLabel()
    return fnamemodify(bufname(winbufnr(1)), ":t")
endfunction

set guitablabel=%!GuiTabLabel()
set mouse=a
let g:prettier#autoformat_require_pragma = 0
let g:prettier#autoformat = 1
