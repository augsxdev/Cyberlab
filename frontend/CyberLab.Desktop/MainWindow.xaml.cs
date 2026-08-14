using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Windows;

namespace CyberLab.Desktop;
public partial class MainWindow : Window
{
    private readonly HttpClient _http = new() { BaseAddress = new Uri("http://127.0.0.1:8000") };
    public MainWindow() => InitializeComponent();

    private async void StartScan_Click(object sender, RoutedEventArgs e)
    {
        try
        {
            ResultText.Text = "Analisando...";
            var body = JsonSerializer.Serialize(new { target = TargetInput.Text, consent = true });
            using var response = await _http.PostAsync("/api/scan", new StringContent(body, Encoding.UTF8, "application/json"));
            var content = await response.Content.ReadAsStringAsync();
            if (!response.IsSuccessStatusCode) throw new HttpRequestException(content);
            StatusText.Text = "Conectada"; StatusText.Foreground = System.Windows.Media.Brushes.LightGreen;
            ResultText.Text = "Scan concluído. Consulte o histórico pela API.";
        }
        catch (Exception ex) { ResultText.Text = $"Erro: {ex.Message}"; }
    }
}
