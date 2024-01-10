input_name=$1
filepath=$(basename -- "$1")
extension="${filepath##*.}"
filename="${filepath%.*}"
output_name="${filename}_music.mp3"
# duration=$(ffprobe -i "$input_name" -show_entries format=duration -v quiet -of csv="p=0")

echo "Input path: ${filepath}"
echo "Extension: ${extension}"
echo "Filename: ${filename}"
echo "Output filename: ${output_name}"
# echo "Duration: ${duration}"
echo
echo

ffmpeg -i "$input_name" -stream_loop -1 -i background.mp3 \
	-joint_stereo 1 -c:v copy -b:a 192k -filter_complex \
	"aevalsrc=0:d=10[s1]; \
	[0:a]volume=volume=1[volume0]; \
	[1:a]volume=volume=-25dB[volume1]; \
	[s1][volume0]concat=n=2:v=0:a=1[amixed1]; \
	[amixed1][volume1]amix=inputs=2:duration=first" "$output_name"
