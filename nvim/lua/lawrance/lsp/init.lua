local status_ok, _ = pcall(require, "lspconfig")
if not status_ok then
	return
end

require("lawrance.lsp.lsp-installer")
require("lawrance.lsp.handlers").setup()
