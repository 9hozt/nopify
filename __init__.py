from binaryninja import *

def do_the_job(bv):
	# Generating imported function symbol list
	imported_syms = bv.get_symbols_of_type("ImportedFunctionSymbol")
	syms = [i.name for i in imported_syms]
	choice_f = ChoiceField("Symbol", syms)

	# Get user choice
	a = get_form_input(["Get Data", None, choice_f], "The options")
	to_nop = syms[choice_f.result]
	sym_addr = bv.get_symbols_by_name(to_nop,ordered_filter=[2])[0].address

	# Get all code xref and patch as NOP
	refs = bv.get_code_refs(sym_addr)
	for ref in refs:
		bv.convert_to_nop(ref.address)

PluginCommand.register("Nopify", "Patch func call to NOP", do_the_job)
