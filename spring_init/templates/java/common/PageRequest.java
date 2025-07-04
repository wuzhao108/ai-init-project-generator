package {{ config.package }}.common;

{% if 'swagger' in config.tech_stack.docs %}
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
{% endif %}

import javax.validation.constraints.Max;
import javax.validation.constraints.Min;
import java.io.Serializable;

/**
 * 分页查询请求
 * 
 * @author {{ config.name }}
 * @since {{ "now" | strftime("%Y-%m-%d") }}
 */
{% if 'swagger' in config.tech_stack.docs %}
@ApiModel(description = "分页查询请求")
{% endif %}
public class PageRequest implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 页码（从1开始）
     */
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "页码（从1开始）", example = "1")
    {% endif %}
    @Min(value = 1, message = "页码不能小于1")
    private Integer pageNum = 1;

    /**
     * 每页大小
     */
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "每页大小", example = "10")
    {% endif %}
    @Min(value = 1, message = "每页大小不能小于1")
    @Max(value = 100, message = "每页大小不能大于100")
    private Integer pageSize = 10;

    /**
     * 排序字段
     */
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "排序字段", example = "createTime")
    {% endif %}
    private String orderBy;

    /**
     * 排序方向（asc/desc）
     */
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "排序方向（asc/desc）", example = "desc")
    {% endif %}
    private String orderDirection = "desc";

    /**
     * 获取页码
     * 
     * @return 页码
     */
    public Integer getPageNum() {
        return pageNum;
    }

    /**
     * 设置页码
     * 
     * @param pageNum 页码
     */
    public void setPageNum(Integer pageNum) {
        this.pageNum = pageNum;
    }

    /**
     * 获取每页大小
     * 
     * @return 每页大小
     */
    public Integer getPageSize() {
        return pageSize;
    }

    /**
     * 设置每页大小
     * 
     * @param pageSize 每页大小
     */
    public void setPageSize(Integer pageSize) {
        this.pageSize = pageSize;
    }

    /**
     * 获取排序字段
     * 
     * @return 排序字段
     */
    public String getOrderBy() {
        return orderBy;
    }

    /**
     * 设置排序字段
     * 
     * @param orderBy 排序字段
     */
    public void setOrderBy(String orderBy) {
        this.orderBy = orderBy;
    }

    /**
     * 获取排序方向
     * 
     * @return 排序方向
     */
    public String getOrderDirection() {
        return orderDirection;
    }

    /**
     * 设置排序方向
     * 
     * @param orderDirection 排序方向
     */
    public void setOrderDirection(String orderDirection) {
        this.orderDirection = orderDirection;
    }

    /**
     * 获取偏移量（用于MyBatis分页）
     * 
     * @return 偏移量
     */
    public Integer getOffset() {
        return (pageNum - 1) * pageSize;
    }

    /**
     * 获取排序SQL
     * 
     * @return 排序SQL
     */
    public String getOrderByClause() {
        if (orderBy == null || orderBy.trim().isEmpty()) {
            return "";
        }
        return orderBy + " " + orderDirection;
    }

    @Override
    public String toString() {
        return "PageRequest{" +
                "pageNum=" + pageNum +
                ", pageSize=" + pageSize +
                ", orderBy='" + orderBy + '\'' +
                ", orderDirection='" + orderDirection + '\'' +
                '}';
    }
}