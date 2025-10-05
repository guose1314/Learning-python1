using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ping测试
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }



        private void Form2_Load(object sender, EventArgs e)
        {
   
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
            // 获取系统内所有进程  
            System.Diagnostics.Process[] currentprocess = System.Diagnostics.Process.GetProcesses();
            foreach (System.Diagnostics.Process p in currentprocess)
            {
                listBox1.Items.Add(p.ToString());
               // System.Console.WriteLine(p.ToString());
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //结束进程
            if (listBox1.Items.Count > 0)
            {
                string a = listBox1.SelectedItem.ToString();
                int indexS = a.IndexOf("(");//获取到从0到“（”的长度
                int indexE = a.IndexOf(")");//获取到从0到“）”的长度
                if (indexS >= 0)
                {
                    string b = a.Substring(indexS + 1, indexE - indexS - 1);
                    textBox2.Text = b;
                    System.Diagnostics.Process[] killprocess = System.Diagnostics.Process.GetProcessesByName(b);
                    foreach (System.Diagnostics.Process p in killprocess)
                    {
                        p.Kill();
                        listBox1.Items.Remove(listBox1.SelectedItem);
                        textBox1.Text = "进程已删除";
                    }
                }
            }
        }
        

        private void button3_Click(object sender, EventArgs e)
        {
                //首先判断列表框中的项是否大于0
            if (listBox1.Items.Count > 0) 
                 {
                 //清空所有项
                     listBox1.Items.Clear();
                 }
        }

        private void listBox1_MouseClick(object sender, MouseEventArgs e)
        {
            textBox1.Text = listBox1.SelectedItem.ToString();
        }
    }
}
    

