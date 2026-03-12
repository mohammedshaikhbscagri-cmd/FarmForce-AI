import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/user_model.dart';
import '../config/api_config.dart';
import 'auth_provider.dart';

class UserState {
  final UserModel? user;
  final bool isLoading;
  final String? error;

  UserState({this.user, this.isLoading = false, this.error});
}

class UserNotifier extends StateNotifier<UserState> {
  final apiService;

  UserNotifier(this.apiService) : super(UserState());

  Future<void> fetchProfile() async {
    state = UserState(isLoading: true);
    try {
      final response = await apiService.get(ApiConfig.me);
      state = UserState(user: UserModel.fromJson(response.data as Map<String, dynamic>));
    } catch (e) {
      state = UserState(error: e.toString());
    }
  }

  Future<void> updateProfile(Map<String, dynamic> data) async {
    state = UserState(user: state.user, isLoading: true);
    try {
      final response = await apiService.put(ApiConfig.me, data: data);
      state = UserState(user: UserModel.fromJson(response.data as Map<String, dynamic>));
    } catch (e) {
      state = UserState(user: state.user, error: e.toString());
    }
  }
}

final userProvider = StateNotifierProvider<UserNotifier, UserState>((ref) {
  return UserNotifier(ref.read(apiServiceProvider));
});
