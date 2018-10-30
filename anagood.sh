module load gcc
function ana(){
cat >ana$j<<EOF
&ana.x
filename=dump$1.xyz, 
cell=10, 
solution_list=cadata.txt, 
auto_velocity=0, 
polarization=1, 
temp=$1,
/
EOF
./ana.x < ana$1
cp result.txt info$1.txt
}
declare -a concent=( 0.30 0.60 0.80 )
declare -a t=( 80 90 120 160 200 240 );
path=/work/jiahaoz/moldy/moldy_files/step3_moldy/BCZO/testall;
path2=`pwd`;
for j in ${t[@]}
do
for i in ${concent[@]}
do
cd $path2/$i
cp $path/ana.x $path2/$i
( ana $j )&
done
wait
done
