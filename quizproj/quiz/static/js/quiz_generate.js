$(document).ready(function () {
    let q_id=1;
    let q_count=1;
    $('#btn_add').click(function (e) { 
        q_count++;
        q_id++;
        let question=`
    <div class="qn card" id="div_qn${q_id}">
            <div class="card-header cu_bg">
            <input type="text" name="q[]" class="quiz_quest in_des" placeholder="Enter question" required/>
            <button class="qn_remove" data-rm="${q_id}">Remove Question</button>
        </div>
       
        <div class="option">
            <ul class="list-group list-group-flush">
                <li class="list-group-item cu_li"><input type="radio" name="ans[${q_id}]"  id="" checked value="0"><input type="text" name="options[]" id="" class="in_des"placeholder="option 1" required></li>
                <li class="list-group-item cu_li"><input type="radio" name="ans[${q_id}]" id=""value="1"><input type="text" name="options[]" id="" class="in_des"placeholder="option 2" required></li>
                <li class="list-group-item cu_li"><input type="radio" name="ans[${q_id}]" id=""value="2"><input type="text" name="options[]" id=""class="in_des" placeholder="option 3" required></li>
                <li class="list-group-item cu_li"><input type="radio" name="ans[${q_id}]" id=""value="3"><input type="text" name="options[]" id="" class="in_des"placeholder="option 4" required></li>
            </ul>
        </div>
    </div>
        `;
        $('#q_container').append(question);
        
    });
    $('#q_container').on('click','.qn_remove', function () {
        q_count--;
        let id=$(this).data('rm');
        $(`#div_qn${id}`).remove();
    });
});