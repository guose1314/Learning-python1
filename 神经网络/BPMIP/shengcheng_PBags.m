function PBags = shengcheng_PBags(bagInf, instanceInf)
%本函数用于 生成 正包 ：第1到第47个正包做正包的训练集
%要生成MUSK2的正包，可改参数。
%2012/09/24    芮辰

bag_pointer = 0;  %包指针
ins_pointer = 1;    %示例指针

num_pos=47;     %正包数
num_neg=45;     %反包数
num_pos_ins =207;   %正示例数

PBags= {};        %初始化正包
 
for i = 1 : num_pos
    bag_pointer = bag_pointer + 1;
    for j = 1 : instanceInf(i)
        PBags{bag_pointer, 1} (j, :) = bagInf(ins_pointer, :);       %生成正训练包的 cell array
        ins_pointer= ins_pointer + 1;
    end  
end

% bag_pointer=0;
% ins_pointer=1;
% ins_pointer = ins_pointer + num_pos_ins;      %所有正包共 num_pos_ins=207示例，前10个负包做测试共35个示例，所以ins_pointer从207+35+1开始
% 
% for i = (num_pos +1) : (num_pos + num_neg)
%     bag_pointer = bag_pointer + 1;
%     
%     for j = 1 : instanceInf(i)
%         NBags{bag_pointer, 1} (j, :) = bagInf(ins_pointer, :);    %生成反包的 cell array
%         ins_pointer= ins_pointer + 1;
%     end
%     
% end
    