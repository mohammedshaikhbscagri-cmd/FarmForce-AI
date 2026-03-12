import '../config/api_config.dart';
import 'api_service.dart';

class AuthService {
  final ApiService _api;

  AuthService(this._api);

  Future<String> sendOtp(String phone) async {
    final response = await _api.post(ApiConfig.sendOtp, data: {'phone': phone});
    return response.data['session_id'] as String;
  }

  Future<Map<String, dynamic>> verifyOtp(
      String phone, String otp, String sessionId) async {
    final response = await _api.post(
      ApiConfig.verifyOtp,
      data: {'phone': phone, 'otp': otp, 'session_id': sessionId},
    );
    final token = response.data['access_token'] as String?;
    if (token != null) {
      _api.setToken(token);
    }
    return response.data as Map<String, dynamic>;
  }

  void signOut() {
    _api.clearToken();
  }
}
