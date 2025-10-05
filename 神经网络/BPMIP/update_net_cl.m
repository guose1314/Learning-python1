function [y,updated]=update_net_cl(net,example,alpha,beta,indicator)
%Adjusting the weights and biases of the BP-MIP 'net' using 'example', 'alpha', 'beta' and 'indicator'

%reading parameters of the network
size_of_inputWeights=net.inputWeights{1}.size;
size_of_layerWeights=net.layerWeights{2,1}.size;
size_of_input=net.inputs{1}.size;
size_of_hiddenlayer=net.layers{1}.size;
size_of_outputs=net.outputs{2}.size;

%initializing delta matrix
delta_inputWeights=zeros(size_of_inputWeights);
delta_layerWeights=zeros(size_of_layerWeights);
delta_hiddenbiases=zeros(size_of_hiddenlayer,1);
delta_outputbiases=zeros(size_of_outputs,1);

%Adjusting weights and biases
sim_out=sim(net,example);
update=0;
if(indicator==1)
   if(max(sim_out)<0.9)
      [real_output,index]=max(sim_out);
      cjk=0.9;
      update=1;
   end
else
   if(max(sim_out)>0.1)
      [real_output,index]=max(sim_out);
      cjk=0.1;
      update=1;
   end
end

if(update==1)
   cur_example=example(:,index);
   bi=logsig(net.IW{1}*cur_example+net.b{1});
   cj=logsig(net.LW{2,1}*bi+net.b{2});
   if(abs(cj-real_output)>=1e-5)
      error('fatal error,program terminates');
   end
   dj=cj*(1-cj)*(cjk-cj);
   ei=zeros(size_of_hiddenlayer,1);
   LayerWeight=net.LW{2,1};
   for i=1:size_of_hiddenlayer
      ei(i)=bi(i)*(1-bi(i))*LayerWeight(1,i)*dj;
   end
   for i=1:size_of_hiddenlayer
      delta_layerWeights(1,i)=alpha*dj*bi(i);
   end
   temp=size_of_inputWeights;
   for h=1:temp(2)
      for i=1:temp(1)
         delta_inputWeights(i,h)=beta*ei(i)*cur_example(h,1);
      end
   end
   delta_outputbiases(1,1)=alpha*dj;
   for i=1:size_of_hiddenlayer
      delta_hiddenbiases(i,1)=beta*ei(i);
   end
   net.IW{1}=net.IW{1}+delta_inputWeights;
   net.LW{2,1}=net.LW{2,1}+delta_layerWeights;
   net.b{1}=net.b{1}+delta_hiddenbiases;
   net.b{2}=net.b{2}+delta_outputbiases;
end

y=net;
updated=update;
      

         