import '../config/api_config.dart';
import 'api_service.dart';

class WeatherService {
  final ApiService _api;

  WeatherService(this._api);

  Future<List<Map<String, dynamic>>> getForecast(
      double lat, double lng) async {
    final response = await _api.get(
      ApiConfig.laborDemand,
      params: {'lat': lat, 'lng': lng},
    );
    return List<Map<String, dynamic>>.from(
        response.data['forecast'] as List? ?? []);
  }
}
