package {{ config.package }}.common;

{% if config.tech_stack.doc %}
import io.swagger.v3.oas.annotations.media.Schema;
{% endif %}

/**
 * 统一响应结果
 * 
 * @author {{ config.name }}
 * @since 2024-01-01
 */
{% if config.tech_stack.doc %}
    @Schema(description = "统一响应结果")
    {% endif %}
public class Result<T> {
    
    {% if config.tech_stack.doc %}
    @Schema(description = "响应码")
    {% endif %}
    private Integer code;
    
    {% if config.tech_stack.doc %}
    @Schema(description = "响应消息")
    {% endif %}
    private String message;
    
    {% if config.tech_stack.doc %}
    @Schema(description = "响应数据")
    {% endif %}
    private T data;
    
    public Result() {}
    
    public Result(Integer code, String message) {
        this.code = code;
        this.message = message;
    }
    
    public Result(Integer code, String message, T data) {
        this.code = code;
        this.message = message;
        this.data = data;
    }
    
    public static <T> Result<T> success() {
        return new Result<>(200, "操作成功");
    }
    
    public static <T> Result<T> success(T data) {
        return new Result<>(200, "操作成功", data);
    }
    
    public static <T> Result<T> success(String message, T data) {
        return new Result<>(200, message, data);
    }
    
    public static <T> Result<T> error() {
        return new Result<>(500, "操作失败");
    }
    
    public static <T> Result<T> error(String message) {
        return new Result<>(500, message);
    }
    
    public static <T> Result<T> error(Integer code, String message) {
        return new Result<>(code, message);
    }
    
    public Integer getCode() {
        return code;
    }
    
    public void setCode(Integer code) {
        this.code = code;
    }
    
    public String getMessage() {
        return message;
    }
    
    public void setMessage(String message) {
        this.message = message;
    }
    
    public T getData() {
        return data;
    }
    
    public void setData(T data) {
        this.data = data;
    }
}