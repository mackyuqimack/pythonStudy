$files = Get-ChildItem -Path 'F:\script' -Recurse
foreach ($file in $files) 
{
    # 创建时间
	$file.CreationTime = Get-Date;
	# 最后修改时间
	$file.LastWriteTime = Get-Date;
	# 创建访问时间
	$file.LastAccessTime = Get-Date "2023-11-25 15:24:15";
}