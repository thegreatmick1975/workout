using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json;

namespace WinFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private async void Form1_Load(object sender, EventArgs e)
        {
            var users = await GetUsers();
            dataGridView1.DataSource = users;
        }

        private async Task<User[]> GetUsers()
        {
            using (var client = new HttpClient())
            {
                var response = await client.GetAsync("http://localhost:5000/users");
                response.EnsureSuccessStatusCode();
                var content = await response.Content.ReadAsStringAsync();
                var result = JsonConvert.DeserializeObject<UserList>(content);
                return result.Users;
            }
        }
    }

    public class UserList
    {
        public User[] Users { get; set; }
    }

    public class User
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int Age { get; set; }
    }
}
