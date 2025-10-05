function [PBags,NBags] = shengcheng_trainBags(bagInf, instanceInf)
%本函数用于将数据集处理成训练用包 ：第11~47个正包做正包的训练集，第58到第92个负包做负包的训练集
%而第1~10个正包 和 第48~57个负包 用做测试， 默认处理的数据集为MUSK1，
%要生成MUSK2的正包和反包，可改参数。
%2012/09/04    芮辰

bag_pointer=0;  %包指针
ins_pointer=35;    %示例指针，前10个正包共有34个示例，所以生成的训练用正包从第35个示例~第207个示例

num_pos=47;     %正包数
num_neg=45;     %反包数
num_pos_ins =207;   %正示例数

PBags= {};        %初始化
NBags={};
 
for i = 11 : num_pos
    bag_pointer = bag_pointer + 1;
    
    for j = 1 : instanceInf(i)
        PBags{bag_pointer, 1} (j, :)= bagInf(ins_pointer, :);       %生成正训练包的 cell array
        ins_pointer= ins_pointer + 1;
    end  
end

bag_pointer=0;
ins_pointer=1;
ins_pointer = ins_pointer + num_pos_ins + 35;      %所有正包共num_pos_ins=207示例，前10个负包做测试共35个示例，所以ins_pointer从207+35+1开始

for i = (num_pos +11) : (num_pos + num_neg)
    bag_pointer = bag_pointer + 1;
    
    for j = 1 : instanceInf(i)
        NBags{bag_pointer, 1} (j, :)= bagInf(ins_pointer, :);    %生成反包的 cell array
        ins_pointer= ins_pointer + 1;
    end
    
end
    