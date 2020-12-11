$path = $args[0]
Function rename-file($path, $new_name){
	try{
		Rename-Item -LiteralPath $path $new_name -ErrorAction Stop
		return $TRUE
	} catch {
		return $FALSE
	}
}

Function clean-name($old_name){
	[hashtable[]]$rules = @(
		@{"origin"=" "; "replacement"="_"},
		@{"origin"="ä"; "replacement"="ae"},
		@{"origin"="ü"; "replacement"="ue"},
		@{"origin"="ö"; "replacement"="oe"},
		@{"origin"="Ä"; "replacement"="Ae"},
		@{"origin"="Ü"; "replacement"="Ue"},
		@{"origin"="Ö"; "replacement"="Oe"},
		@{"origin"="\?"; "replacement"=""},
		@{"origin"="!"; "replacement"=""},
		@{"origin"="~"; "replacement"=""},
		@{"origin"="-"; "replacement"="_"},
		@{"origin"="\+"; "replacement"=""},
		@{"origin"="#"; "replacement"="_"},
		@{"origin"="\("; "replacement"="["},
		@{"origin"="@{"; "replacement"="["},
		@{"origin"="\)"; "replacement"="]"},
		@{"origin"="}"; "replacement"="]"})

	$name = $old_name -match "\\(?<filename>[^\\]+\.\w+)"
	$new_name = "$($matches.filename)"

	#apply rules
	foreach($r in $rules)
	{
		$new_name = $new_name -creplace $r["origin"],$r["replacement"]
	}
	#rename file
	$result = $FALSE
	$i = 0
	$extension = ""
	$name = ""
	while(!($result)){
		$result = rename-file -path $path -new_name $new_name
		$parts = $new_name.split(".") #apply number to name of file
		$name = $parts[0]
		$extension = $parts[1]
		$i += 1
		if($i -ge 2){
			$name = $name.substring(0,$name.length-2)
		}
		$name = "${name}_${i}"
		$new_name = "$($name).$($extension)"
	}
	#Add-Type -AssemblyName PresentationFramework
	#[System.Windows.MessageBox]::Show("Hello $path $(Split-Path -Path $path)\$new_name $new_name")
}
clean-name -old_name $path