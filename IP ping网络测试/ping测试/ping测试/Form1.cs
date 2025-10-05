using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.NetworkInformation;
namespace ping测试
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public void huiche() //判断是否按下回车
        {
            button1_Click(null, null);

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            button2.Enabled = false;
            textBox2.Enabled = false;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox2.Enabled != true)
            {

                if (textBox1.Text != "")
                {
                    button1.Enabled = false;
                    button2.Enabled = true;
                    checkBox1.Enabled = false;
                    textBox2.Enabled = false;
                    timer1.Start();
                }
                else
                {
                    MessageBox.Show("请输入IP-如192.168.0.1", "提醒", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
            else
            {
                if (textBox1.Text != "" && textBox2.Text != "")
                {
                    button1.Enabled = false;
                    button2.Enabled = true;
                    checkBox1.Enabled = false;
                    textBox2.Enabled = false;
                    timer2.Start();
                }
                else
                {
                    MessageBox.Show("请输入IP-如(192.168.0.1)\n请输入地址位数-如(1-254)", "提醒", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
        }
        private void button2_Click(object sender, EventArgs e)
        {
            button1.Enabled = true;
            button2.Enabled = false;
            checkBox1.Enabled = true;
            textBox2.Enabled = true;
            timer1.Stop();
            timer2.Stop();
        }

        private void timer1_Tick(object sender, EventArgs e)
        { 
           


                    bool online = false; //是否在线
                    Ping ping = new Ping();
                    string ipstr = textBox1.Text; //获取IP
                    string ipaddss = textBox2.Text;
                    int timeout = 100; //设置超时显示时间
                    //准备测试数据
                    string data = "test data";
                    byte[] buffer = Encoding.ASCII.GetBytes(data);

                    //数据发送开始
                    PingReply pingReply = ping.Send(ipstr, timeout, buffer);
                    if (pingReply.Status == IPStatus.Success)
                    {
                        online = true;
                        //MessageBox.Show("当前在线，已ping通！");

                    }
                    string txt = "";
                    if (online)
                    {
                        txt = "当前在线，已ping通！" + "   IP—" + ipstr + "   时间--" + DateTime.Now.ToString();
                        listBox1.Items.Insert(0, txt);
                    }
                    else
                    {
                        txt = "不在线，ping不通！" + "   IP—" + ipstr + "    时间--" + DateTime.Now.ToString();
                        listBox2.Items.Insert(0, txt);
                    }
                }
                
                
                      
        


        private void button3_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();

        }
        private void button4_Click(object sender, EventArgs e)
        {
            listBox2.Items.Clear();
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == 13)//判断是否按下回车
            {
                huiche();
            }
            //如果输入的不是数字键，也不是回车键、Backspace键，则取消该输入
            //if (!(Char.IsNumber(e.KeyChar)) && e.KeyChar != (char)13 && e.KeyChar != (char)8)
            //{
            //    e.Handled = true;
            //}
        }
        private void textBox2_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == 13)//判断是否按下回车
            {
                huiche();
            }
            //如果输入的不是数字键，也不是回车键、Backspace键，则取消该输入
            //if (!(Char.IsNumber(e.KeyChar)) && e.KeyChar != (char)13 && e.KeyChar != (char)8)
            //{
            //    e.Handled = true;
            //}
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked) //检测是否勾选
            {
                textBox2.Enabled = true;
            }
            else
            {
                textBox2.Enabled = false;
                textBox2.Text = "";
            }

        }

        private void timer2_Tick(object sender, EventArgs e)
        {
               

                  
                    Ping ping = new Ping();
                    string ipstr = textBox1.Text; //获取IP
                    string ipaddss = textBox2.Text; //获取地址位数
                    string[] FENKAI = ipstr.Split('.');
                    int fenkai = Convert.ToInt32(FENKAI[3]);//将STRING类型的转成INT型取第3数组里面的内容
                    int dizhi = Convert.ToInt32(ipaddss);
                    int timeout = 100; //设置超时显示时间
                    //准备测试数据
                    string data = "test data";
                    byte[] buffer = Encoding.ASCII.GetBytes(data);
                    int[] name;
                    name = new int[dizhi];

                    for (int ii = fenkai; ii <= dizhi; ii++)
                    {
                       
                        for (int i = 0; i <= dizhi; i++)
                        {
                            name[i] = ii;
                            break;

                        }
                        bool online1 = false;
                        //数据发送开始
                        string ip = ipstr.Substring(0, ipstr.LastIndexOf(".") + 1);
                        string ipp = ip + name[0];
                        PingReply pingReply = ping.Send(ipp, timeout, buffer);
                        if (pingReply.Status == IPStatus.Success)
                        {
                            online1 = true;
                            //MessageBox.Show("当前在线，已ping通！");

                        }
                        string txt = "";
                        if (online1)
                        {
                            txt = "当前在线，已ping通！" + "   IP—" + ipp + "   时间--" + DateTime.Now.ToString();
                            listBox1.Items.Insert(0, txt);
                           
                        }
                        else
                        {
                            txt = "不在线，ping不通！" + "   IP—" + ipp + "    时间--" + DateTime.Now.ToString();
                            listBox2.Items.Insert(0, txt);
                        }
                      

                    }
                
            }
          
        }


    }

        

   
    
     
        
    

