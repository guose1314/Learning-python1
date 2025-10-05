function [net,outputs] = BP_MIP(PBags,NBags,testBags,epoch_num,alpha,beta,hidden_neuron)
% function [net,outputs] = BP_MIP(PBags,NBags,testBags,950,0.05,0.05,950)

%  BP_MIP  Using the BP-MIP algorithm[1] to get the labels for bags in testBags
%     BP_MIP takes,
%        PBags         - an Mx1 cell array where the jth instance of ith positive bag is stored in PBags{i}(j,:)
%        NBags         - an Nx1 cell array where the jth instance of ith negative bag is stored in NBags{i}(j,:)
%        testBags      - a Kx1 cell array where the jth instance of ith test bag is stored in testBags{i}(j,:)
%        epoch_num     - the number of training epochs for BP_MIP, training epochs varies from 50 to 1,000 with an interval of 50
%        alpha         - learning rate for the first layer weights  0.05
%        beta          - learning rate for the second layer weights  0.05
%        hidden_neuron - number of hidden units,80 hidden units and 950 training epochs.
%          
%        learning rate is set to 0.05
%     and returns,
%        net      -  the trained neural network
%        outputs  -  the output predicted by net on the i-th testBag is stored in outputs(1,i)
%
% For more details, please reference to bibliography [1]
% [1] Z.-H. Zhou and M.-L. Zhang. Neural networks for multi-instance learning. Technical Report, AI Lab, Computer
%     Science&Techlonogy Department, Nanjing University, Nanjing, China, 2002.

   if(nargin<=6)
       error('not enough input parameters');
   end

%  0-1 normalization for training and testing data

%  grouping all the instances in training and testing bags   
   temp_pointer=0;
   all_inst=[];
   
   tempsize=size(PBags);
   num_pbags=tempsize(1);
   for i=1:num_pbags
      all_inst=[all_inst;PBags{i,1}];
      temp_pointer=temp_pointer+1;
      bag_size=size(PBags{i,1});
      mole_num(1,temp_pointer)=bag_size(1);
   end
   
   tempsize=size(NBags);
   num_nbags=tempsize(1);
   for i=1:num_nbags
      all_inst=[all_inst;NBags{i,1}];
      temp_pointer=temp_pointer+1;
      bag_size=size(NBags{i,1});
      mole_num(1,temp_pointer)=bag_size(1);
   end

   tempsize=size(testBags);
   num_testbags=tempsize(1);
   for i=1:num_testbags
      all_inst=[all_inst;testBags{i,1}];
      temp_pointer=temp_pointer+1;
      bag_size=size(testBags{i,1});
      mole_num(1,temp_pointer)=bag_size(1);
   end
  
   all_inst=min_max_norm(0,1,all_inst);

%  restoring all the instances in training and testing bags
   temp_pointer=0;
   for i=1:num_pbags
      temp_pointer=temp_pointer+1;
      PBags{i,1}=all_inst((sum(mole_num(1:temp_pointer-1))+1):sum(mole_num(1:temp_pointer)),:);
   end
   for i=1:num_nbags
      temp_pointer=temp_pointer+1;
      NBags{i,1}=all_inst((sum(mole_num(1:temp_pointer-1))+1):sum(mole_num(1:temp_pointer)),:);
   end
   for i=1:num_testbags
      temp_pointer=temp_pointer+1;
      testBags{i,1}=all_inst((sum(mole_num(1:temp_pointer-1))+1):sum(mole_num(1:temp_pointer)),:);
   end

%  initializing BP-MIP network
   tempsize=size(PBags{1,1});
   attribute_num = tempsize(2);

   min_max = zeros(attribute_num, 2);
   min_max(:,2)=1;   

   rand('state',sum(100*clock));%set initial seed for the random fucntion
   incremental=ceil(rand*100);
   for randpos=1:incremental
       net=newff(min_max, [hidden_neuron,1],{'logsig','logsig'});
     % net=newff(min_max, output, [hidden_neuron,1],{'logsig','logsig'});
   end   

   for epochs=1:epoch_num
      for pbags=1:num_pbags
          [net,updated]=update_net_cl(net,PBags{pbags,1}',alpha,beta,1);
      end
   end
      for nbags=1:num_nbags
          [net,updated]=update_net_cl(net,NBags{nbags,1}',alpha,beta,0);
      end   
   end

   outputs=-ones(1,num_testbags);
   for i=1:num_testbags
       outputs(1,i)=(max(sim(net,testBags{i,1}'))>=0.5);
   end