// --- ✨ 新增: 取得或建立 Session ID ---
// 這會生成一個隨機 ID 並存在瀏覽器裡 (localStorage)
function getSessionId() {
  let sessionId = localStorage.getItem("chat_session_id");
  if (!sessionId) {
    // 如果沒有 ID，就生成一個新的 (例如: user_1701234567_abcde)
    sessionId = "user_" + Date.now() + "_" + Math.random().toString(36).substr(2, 9);
    localStorage.setItem("chat_session_id", sessionId);
  }
  return sessionId;
}