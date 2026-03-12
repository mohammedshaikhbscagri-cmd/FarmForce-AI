import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/user_model.dart';
import '../services/api_service.dart';
import '../services/auth_service.dart';
import '../config/api_config.dart';

final apiServiceProvider = Provider<ApiService>((ref) => ApiService());

final authServiceProvider = Provider<AuthService>((ref) {
  return AuthService(ref.read(apiServiceProvider));
});

class AuthState {
  final UserModel? user;
  final bool isLoading;
  final String? error;

  AuthState({this.user, this.isLoading = false, this.error});
}

class AuthNotifier extends StateNotifier<AuthState> {
  final AuthService _authService;
  final ApiService _apiService;

  AuthNotifier(this._authService, this._apiService) : super(AuthState());

  Future<String> login(String phone) async {
    state = AuthState(isLoading: true);
    try {
      final sessionId = await _authService.sendOtp(phone);
      state = AuthState();
      return sessionId;
    } catch (e) {
      state = AuthState(error: e.toString());
      rethrow;
    }
  }

  Future<void> verifyOtp(String phone, String otp, String sessionId) async {
    state = AuthState(isLoading: true);
    try {
      final data = await _authService.verifyOtp(phone, otp, sessionId);
      if (data['user'] != null) {
        state = AuthState(user: UserModel.fromJson(data['user'] as Map<String, dynamic>));
      } else {
        state = AuthState();
      }
    } catch (e) {
      state = AuthState(error: e.toString());
      rethrow;
    }
  }

  Future<void> checkAuth() async {
    // TODO: Load token from SharedPreferences and validate
  }

  void logout() {
    _authService.signOut();
    state = AuthState();
  }
}

final authProvider = StateNotifierProvider<AuthNotifier, AuthState>((ref) {
  return AuthNotifier(
    ref.read(authServiceProvider),
    ref.read(apiServiceProvider),
  );
});
