@app.post("/chat")
async def chat_endpoint(req: UserRequest):
    try:
        user_id = req.session_id
        
        # 1. 如果這個人沒來過，幫他開一本新筆記
        if user_id not in user_sessions:
            user_sessions[user_id] = []
            
        # 2. 拿出他的專屬紀錄
        chat_history = user_sessions[user_id]

        # 3. 呼叫 RAG (把紀錄也傳進去！)
        # 注意：這裡假設您的 RAG 鏈支援 chat_history 參數
        result = qa_chain.invoke({
            "question": req.message,
            "chat_history": chat_history 
        })
        
        answer = result['answer']

        # 4. 把這次的問答寫回筆記本
        user_sessions[user_id].append((req.message, answer))
        
        # (選用) 為了避免筆記本太厚，只留最後 10 句
        if len(user_sessions[user_id]) > 10:
             user_sessions[user_id] = user_sessions[user_id][-10:]

        return {"reply": answer}